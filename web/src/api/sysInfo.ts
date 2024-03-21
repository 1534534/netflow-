import {get, post} from '/@/utils/http/axios';

enum URL {
    sysInfo= '/myapp/admin/sysInfo/sysInfo',
}


const sysInfoApi = async (params: any) =>
    get<any>({url: URL.sysInfo, params: params, data: {}, headers: {}});

export {sysInfoApi};
