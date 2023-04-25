import React, {useEffect, useState} from "react";
import {CircularProgress, Grid} from "@mui/material";
import CardExposition from "../../components/Exposition/CardExposition";
import Box from "@mui/material/Box";
import dataFetch from "../../components/utils/dataFetch";

const Expositions = () => {
    const apiLink = '/frontend/api/exposition_list'
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);

    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {is_archive:0}, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [])

    return (
        <>
            {function (){

                if (fetchAll){
                    return (
                        <Box sx={{display: 'flex'}}>
                <Grid container spacing={2}
                      sx={{justifyContent: data.length > 2 ? 'space-between' : 'flex-start'}}>
                    {data.map((item, index) => (

                        <Grid item xs="auto"
                              key={index}>
                            <CardExposition
                                data={item}/>
                        </Grid>

                    ))}
                </Grid>
            </Box>
                    )
                } else{
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