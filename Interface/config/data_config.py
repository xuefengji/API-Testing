
class global_var:
    #定义excel表格中列的值的id
    case_id = 0
    module_name = 1
    url = 2
    is_run = 3
    request_way = 4
    header = 5
    case_depend = 6
    responsere_depend = 7
    data_depend = 8
    requset_data = 9
    expact_result = 10
    result = 11

#获取各个单元格数据的ID
def get_case_id():
    return global_var.case_id

def get_module_name():
    return global_var.module_name

def get_url():
    return global_var.url

def get_header():
    return global_var.header

def get_case_depend():
    return global_var.case_depend

def get_request_way():
    return global_var.request_way

def get_data_depand():
    return global_var.responsere_depend

def request_data():
    return global_var.data_depend

def get_method_request_data():
    return global_var.requset_data

def get_expact_result():
    return global_var.expact_result

def get_result():
    return global_var.result

def get_is_run():
    return global_var.is_run
