import * as React from 'react';
import axios from "axios";


function fetching(value){
    return ()=>{}
}

const dataFetch = (url, params, callback) => {

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
        }).then((data)=>{callback(data)})
        .catch((e) => {
            console.log(e);
        });

}
export default dataFetch

