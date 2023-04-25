import React, {useEffect, useState} from "react";

const Expositions=()=>{
    const apiLink = '/frontend/api/expositions/'
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);

    return (
        <>
            <h2>Expositions base</h2>
        </>
    )
}


export {Expositions}