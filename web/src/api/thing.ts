// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
    list = '/myapp/admin/thing/list',
    update = '/myapp/admin/thing/update',
  
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });

const updateApi = async (params:any, data: any) =>
    post<any>({ url: URL.update,params: params, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });

export { listApi, updateApi };
