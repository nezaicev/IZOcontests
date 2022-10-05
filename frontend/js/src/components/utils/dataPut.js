import axios from "axios";

const dataPut = (url,params, jsonData, callback) => {
    let status = ''
    let data = []

    if (!url) return;
    status = 'sending'
    axios({
        method: "PUT",
        url: url,
        params: params,
        data: jsonData,
    })
        .then((res) => {
            data = res.data
            status = 'sanded'
            return data
        }).then((data)=>{callback(data)})
        .catch((e) => {
            console.log(e);
        });

}
export default dataPut