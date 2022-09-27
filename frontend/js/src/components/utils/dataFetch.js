import * as React from 'react';
import axios from "axios";


const dataFetch = (url, params, callback, fetching) => {
    // status ? status = true:''
    fetching(true)
    let data = []

    if (!url) return;
    axios({
        method: "GET",
        url: url,
        params: params,
    })
        .then((res) => {
            data = res.data
            return data
        }).then((data)=>{callback(data);fetching(false)})
        .catch((e) => {
            console.log(e);
        });

}
export default dataFetch

