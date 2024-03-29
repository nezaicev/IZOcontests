import React, {useEffect, useState} from "react";
import dataFetch from "../../components/utils/dataFetch";
import Box from "@mui/material/Box";
import {CircularProgress, Paper, Typography} from "@mui/material";


const VP=()=>{
    const apiLink = '/frontend/api/page/vp_base_info/'
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);

    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {}, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [])
    return (
         <Box>{
                            fetchAll ? <Box>
                                <Box sx={{
                                    justifyContent: 'center',
                                    display: 'flex',
                                    marginTop: '30px',
                                    marginBottom: '20px'
                                }}>
                                    <Typography variant="h5">
                                        {data.subtitle}
                                    </Typography>
                                </Box>


                                <Paper

                                    dangerouslySetInnerHTML={{__html: data.content}}
                                    scroll={'body'}
                                    sx={{
                                        boxShadow: 0,
                                        overflow: 'auto',
                                        padding: ['5px', '15px'],
                                    }}

                                />


                            </Box> : <Box sx={{
                                justifyContent: 'center',
                                height: '600',
                                display: 'flex',
                                marginTop: ' 20px'
                            }}>
                                <CircularProgress sx={{
                                    color: '#d26666'
                                }}/>
                            </Box>
                        }</Box>
    )
}

export {VP}