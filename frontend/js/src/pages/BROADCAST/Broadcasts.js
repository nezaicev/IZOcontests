import {CircularProgress, Grid} from "@mui/material";
import ItemBroadcast from "../../components/Broadcast/ItemBroadcast";
import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import {useOutletContext} from "react-router-dom";
import dataFetch from "../../components/utils/dataFetch";

const Broadcasts = () => {
    const apiLink = '/frontend/api/broadcasts/'

    const [fetchAll, setFetchAll] = useState(false);
    const [data, setData] = React.useState([])
    const auth = useOutletContext()


    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, null, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [])


    return (function () {
            if (fetchAll) {
                return (
                    <Box sx={{
                        display: 'grid',
                        gridTemplateColumns: `repeat(auto-fill, minmax(320px, 1fr))`,
                        justifyItems: 'center',
                        alignItems: 'stretch',
                        marginBottom: '30px',

                    }}>
                        {data.map((item, index) => (
                            item['broadcast_url'] ?
                                <Grid item xs="auto" sx={{}}
                                      key={index}>
                                    <ItemBroadcast
                                        data={item}/>
                                </Grid> : ''
                        ))}

                    </Box>)

            } else {
                return (
                    <Box sx={{
                        justifyContent: 'center',
                        height: '600',
                        display: 'flex',
                        marginTop: ' 20px'
                    }}>
                        <CircularProgress sx={{
                            color: '#d26666'
                        }}/>
                    </Box>
                )
            }

        }()

    )
}


export {Broadcasts}