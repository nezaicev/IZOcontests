import React, {useEffect, useState} from "react";
import {CircularProgress, Grid} from "@mui/material";
// import CardExposition from "../../components/Exposition/CardExposition";
import Box from "@mui/material/Box";
import dataFetch from "../../components/utils/dataFetch";

import {lazy, Suspense} from 'react';
const CardExposition = lazy(() => import('../../components/Exposition/CardExposition'));


const Expositions = (props) => {
    const apiLink = '/frontend/api/exposition_list'
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);
    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {is_archive: props.isArchive}, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [])

    useEffect(() => {
        setData([])
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {is_archive: props.isArchive}, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [props.isArchive])


    return (
        <>
            {function () {

                if (fetchAll
                    || data.length >0) {
                    return (
                        <Box sx={{display: 'flex'}}>
                            <Grid container spacing={2}
                                  sx={{justifyContent: data.length > 2 ? 'space-between' : 'flex-start'}}>
                                {data.map((item, index) => (

                                    <Grid item xs="auto"
                                          key={index}>
                                         <Suspense fallback={<div>Загрузка...</div>}>
      <CardExposition
                                            data={item}/>
    </Suspense>
                                        {/*<CardExposition*/}
                                        {/*    data={item}/>*/}
                                    </Grid>

                                ))}
                            </Grid>
                        </Box>
                    )
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

            }()}


        </>
    )
}


export {Expositions}