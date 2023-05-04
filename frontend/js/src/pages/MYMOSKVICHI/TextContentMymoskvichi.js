import React, {useEffect, useState} from "react";
import Box from "@mui/material/Box";
import {CircularProgress, Paper, Typography} from "@mui/material";
import {BaseInfo} from "./BaseInfo";
import dataFetch from "../../components/utils/dataFetch";


const TextContentMymoskvichi=(props)=>{
    const apiLink = props.link
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);

    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {}, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [])
    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {}, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [props.link])


    return (
         <Box>{
                            fetchAll ? <Box>
                                <BaseInfo/>
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

export {TextContentMymoskvichi}