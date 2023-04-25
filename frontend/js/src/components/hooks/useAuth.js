import React, {useEffect} from "react";
import dataFetch from "../utils/dataFetch";
import {host} from "../utils/consts";

const useAuth=()=>{
    const [auth, setAuth] = React.useState({
        "id": '',
        "user": "AnonymousUser",
        "auth": false,
        "superuser": false,
        "manager":false,
    })

    useEffect(() => {
        dataFetch(`${host}/frontend/api/auth/`, null, (data) => {
            setAuth(data);

        })
    }, [])

    return auth
}

export default useAuth