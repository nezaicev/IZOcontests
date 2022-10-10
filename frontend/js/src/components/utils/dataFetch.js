import * as React from 'react';
import axios from "axios";


function fetching(value){
    return ()=>{}
}

const dataFetch = (url, params, callback) => {

    let data = []
    let status=null
    if (!url) return;
    axios({
        method: "GET",
        url: url,
        params: params,
    })
        .then((res) => {
            data = res.data
            status='ok'
            return data
        }).then((data)=>{callback(data)})
        .catch((e) => {
            console.log(e);
        });
        return status
}
export default dataFetch

