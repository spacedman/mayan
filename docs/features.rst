========
Features
========


* Document versioning.

    * Store many versions of the same document, download or revert to a previous version.

* Electronic signature verification.

    * Check the authenticity of documents by verifying their embedded cryptographic signatures or upload detached signatures for document signed after they were stored.

* Collaboration tools.

    * Discuss documents, comment on new version of a document.

* Office document format support.

    * Word processing files?  Spreadsheets?  Sresentations?  They are supported too.

* User defined metadata fields and meta data sets.

    * Metadata fields can be grouped into sets per technical, legal or structural requirements such as the `Dublin core`_
    
.. _`Dublin core`: http://dublincore.org/metadata-basics/
    
* Dynamic default values for metadata.
    
    * Metadata fields can have an initial value which can be static or determined by an user provided Python code snipped.

* Filesystem integration.
    
    * If enabled, the document database index can be mirrored in the filesystem of the hosting computers and shared via Samba_ or any other method to clients computers on a network.
    
.. _Samba:  http://www.samba.org/

* User defined document unique identifier and checksum algorithms.
    
    * Users can alter the default method used to uniquely indentify documents.

* Documents can be uploaded from different sources.

    * Local file or server side file uploads.

* Batch upload many documents with the same metadata.

    * Clone a document's metadata for speedier uploads and eliminate repetitive data entry.

* Previews for a great deal of image formats, including PDF.

    * **Mayan EDMS** provides different file conversion backends with different levels of functionality and requirements to adapt to different deployment environments.

* Full text searching.

    * Document can be searched by their text content, their metadata or any other file attribute such as name, extension, etc.

* Configurable document grouping.
    
    * Automatic linking of documents based on metadata values or document properties.

* Roles support.

    * Users can created an unlimited amount of different roles and are not restricted to the traditional admin, operator, guest paradigm.

* Fine grained permissions system.

    * There is a permission for every atomic operation performed by users.

* Multi page document support.

    * Multiple page PDFs and TIFFs files supported.

* Distributed OCR processing.

    * The task of transcribing text from documents via OCR can be distributed among several physical or virtual computers to decrease load and increase availability.

* Multilingual user interface (English, Spanish, Portuguese, Russian).

    * **Mayan EDMS** is written using the Django_ framework which natively support Unicode, this coupled with the use of text templates allows **Mayan EDMS** to be translated to practically any language spoken in the world, by default four translations are provided: English, Spanish, Portuguese and Russian.
    
.. _Django:  https://www.djangoproject.com/

* Multilingual OCR support.

    * *As supported by the OCR engine tesseract.

* Duplicated document search.

* Plugable storage backends (File based and GridFS included).
    
    * Very easy to convert other 3rd party such as the ones available for Amazon EC2.

* Color coded tagging.

    * Labeled and color coded tags that are intituitive.

* Staging folders to receive scanned documents directly from network attached scanners.

    * Preview scanned files even before uploading them.
