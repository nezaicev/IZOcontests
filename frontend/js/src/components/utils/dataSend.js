import axios from "axios";

const dataSend = (url, params, callback) => {
    let status = ''
    let data = []

    if (!url) return;
    status = 'sending'
    axios({
        method: "POST",
        url: url,
        params: params,
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
export default dataSend