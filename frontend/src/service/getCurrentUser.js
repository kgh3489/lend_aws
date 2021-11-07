import axios from 'axios';

//현재 로그인된 유저정보 가져오기
export function getCurrentUser() {
    
    return axios({
        method: 'get',
        url: '/user/info',
        headers: {
            "Content-Type": "application/json",
            "Authorization": `JWT ${localStorage.getItem('ACCESS_TOKEN')}`
        }
    })
} 