import * as React from 'react';
import axios from "axios";


const dataFetch = (url, params, callback) => {
    let status = ''
    let data = []

    if (!url) return;
    status = 'fetching'
    axios({
        method: "GET",
        url: url,
        params: params,
    })
        .then((res) => {
            data = res.data
            status = 'fetched'
            return data
        }).then((data)=>{callback(data)})
        .catch((e) => {
            console.log(e);
        });

}

export default dataFetch