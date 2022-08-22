import json
import os
import requests
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient



def test_pdf(filename):
    endpoint = "https://frpdf.cognitiveservices.azure.com/"
    key = "1ee5d5cdbeb24d77abefbd48841bd345"

    model = "test_pdf"
    
    document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    with open(filename, "rb") as fd:
        document = fd.read()
    poller = document_analysis_client.begin_analyze_document(model, document)
    result = poller.result()
    
    if type == 'text':
        result = result.content


#poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
#result = poller.result()
    dict = {}
    for idx, document in enumerate(result.documents):
        outer_dict = {}
        for name, field in document.fields.items():
            inner_dict = {}
            field_value = field.value if field.value else field.content
            if field_value is None:
                if name[2:].replace('_', ' ').lower() in result.content.lower():
                    field_value = ''
                    print(field_value)
            inner_dict["FieldValue"] = field_value
            #inner_dict["Confidence"] = field.confidence
            outer_dict[name] = inner_dict
            dict['Field'] = [outer_dict]
            print(dict)
	# dict_page.append(dict)
	#return dict
            with open('data.json','w') as json_file:
                json.dump(dict,json_file,indent = 4)
    return dict

#print("-----------------------------------")

#test_pdf('CERTIFICATE OF LIABILITY INSURANCE.pdf',"https://frpdf.cognitiveservices.azure.com/","1ee5d5cdbeb24d77abefbd48841bd345")







