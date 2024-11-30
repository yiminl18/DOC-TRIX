import random,os 

def get_seed(l,r):
    random_number = random.randint(l, r)
    return random_number

def reverse_node(data): 
    ndata = []
    for record in data:
        nrecord = {}
        id = record['id']
        content = record['content']
        ncontent = []
        for block in content:
            if(block['type'] == 'metadata'):
                continue
            nblock = {}
            ntuples = []
            for tuple in block['content']:
                ntuple = {}
                for k,v in tuple.items():
                    if(get_seed(0,100)<14):#recall, delete this tuple
                        continue
                    if(get_seed(0,100)<18):#precision
                        ntuple[k] = 'missing'
                    else:
                        ntuple[k] = v
                ntuples.append(ntuple)
            nblock['content'] = ntuples 
            nblock['type'] = block['type']
            ncontent.append(nblock)
        nrecord['content'] = ncontent
        nrecord['id'] = id
        ndata.append(nrecord)
        
    return ndata

def reverse_pipeline():
    root_path = get_root_path()
    pdf_folder_path = root_path + '/data/raw/benchmark1'
    pdfs = scan_folder(pdf_folder_path,'.pdf')
    for pdf_path in pdfs:
        truth_path = pdf_path.replace('raw','truths').replace('.pdf','.json')
        if(not os.path.isfile(truth_path)):
            continue
        truth = read_json(truth_path)
        c = reverse_node(truth)
        out_path = pdf_path.replace('data/raw','result').replace('.pdf','.json')
        write_json(c,out_path)
        #break