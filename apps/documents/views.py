import datetime

from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
from django.views.generic.list_detail import object_detail, object_list
from django.core.urlresolvers import reverse
from django.views.generic.create_update import create_object
from django.forms.formsets import formset_factory


from forms import DocumentForm_view

from models import Document, DocumentMetadata, DocumentType, MetadataType
from forms import DocumentTypeSelectForm, DocumentCreateWizard, \
        MetadataForm, DocumentForm
        

def document_list(request):
    return object_list(
        request,
        queryset=Document.objects.all(),
        template_name='generic_list.html',
        extra_context={
            'title':_(u'documents'),
            'extra_columns':[
                {'name':_(u'filename'), 'attribute':'file_filename'},
                {'name':_(u'extension'), 'attribute':'file_extension'},
                {'name':_(u'mimetype'), 'attribute':'file_mimetype'},
                {'name':_(u'added'), 'attribute':'date_added'},
            ],
        },
    )


def document_create(request):
    MetadataFormSet = formset_factory(MetadataForm, extra=0)
    wizard = DocumentCreateWizard(form_list=[DocumentTypeSelectForm, MetadataFormSet])
    return wizard(request)


def upload_document_with_type(request, document_type_id, multiple=True):
    document_type = get_object_or_404(DocumentType, pk=document_type_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, initial={'document_type':document_type})
        if form.is_valid():
            instance = form.save()
            for key, value in request.GET.items():
                document_metadata = DocumentMetadata(
                    document=instance,
                    metadata_type=get_object_or_404(MetadataType, pk=key),
                    value=value
                )
                document_metadata.save()

            messages.success(request, _(u'Document uploaded successfully.'))
            if multiple:
                return HttpResponseRedirect(request.get_full_path())
            else:
                return HttpResponseRedirect(reverse('document_list'))
    else:
        form = DocumentForm(initial={'document_type':document_type})
        
    return render_to_response('generic_form.html', {
        'form':form
    }, context_instance=RequestContext(request))
        
        
def document_view(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    form = DocumentForm_view(instance=document, extra_fields=[
        {'label':_(u'Filename'), 'field':'file_filename'},
        {'label':_(u'File extension'), 'field':'file_extension'},
        {'label':_(u'File mimetype'), 'field':'file_mimetype'},
        {'label':_(u'Date added'), 'field':'date_added'},
    ])
    
    return render_to_response('generic_detail.html', {
        'form':form,
        'object':document,
        'subtemplates_dict':[
            {
                'name':'generic_list_subtemplate.html',
                'title':_(u'metadata'),
                'object_list':document.documentmetadata_set.all(),
                'extra_columns':[{'name':_(u'qty'), 'attribute':'value'}],
                'hide_link':True,
            },
        ],  
    }, context_instance=RequestContext(request))    
    