import axios from "axios";

const dataPost = (url,params, jsonData, callback) => {
    let status = ''
    let data = []
    if (!url) return;
    status = 'sending'
    axios({
        method: "POST",
        url: url,
        params: params,
        data: jsonData,
    })
        .then((res) => {
            data = res.data
            status = 'sanded'
            data['status']=status
            console.log(data,'res')
            return data
        }).then((data)=>{callback(data)})
        .catch((e) => {
            console.log(e);
        });

}
export default dataPost