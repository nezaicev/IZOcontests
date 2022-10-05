import axios from "axios";

const dataDelete = (url, params, callback) => {
    let status = ''
    let data = []

    if (!url) return;
    status = 'sending'
    axios({
        method: "DELETE",
        url: url,
        params:params,
    })
        .then((res) => {
            data = res.data
            status = 'sent'
            return data
        }).then((data)=>{callback(data)})
        .catch((e) => {
            console.log(e);
        });

}
export default dataDelete