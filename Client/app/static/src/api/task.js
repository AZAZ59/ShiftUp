/**
 * Created by vlad on 19.11.16.
 */

var axios = require('axios');

const BASE_API_URL = 'http://0.0.0.0:5000/api/';
const BASE_VK_API_URL = 'https://api.vk.com/method/';


export function send_task(method, args){
    axios.post(BASE_API_URL+'task', {
        method: method,
        args: args
    }).then(function (response) {
        console.log(response);
    }).catch(function (error) {
        console.log(error);
    });
}

export function get_task_list(){
    return axios.get(
        BASE_API_URL+'tasks'
    ).then(function(response){
        return response.data
    })
}

export function get_result_list(result_id){
    return axios.get(
        BASE_API_URL+'tasks/'+result_id.toString()
    ).then(function(response){
        return response.data
    })
}

export function get_user_base_info(uid){
    return axios.get(
        BASE_VK_API_URL+'users.get',{
            params:{
                users_id: uid,
                fields: 'photo'
            }
        }
    ).then(function(response){
        return response.data
    })
}

export function get_group_base_info(gid){
    return axios.get(
        BASE_VK_API_URL+'groups.getById',{
            params:{
                group_id: gid,
                fields: 'photo'
            },
            headers: {'Access-Control-Allow-Origin': '*'}
        }
    ).then(function(response){
        return response.data
    })
}
