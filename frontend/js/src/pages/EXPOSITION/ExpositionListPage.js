import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";

import React, {useEffect, useState} from "react";

import useAuth from "../../components/hooks/useAuth";
import dataFetch from "../../components/utils/dataFetch";
import CardExposition from "../../components/Exposition/CardExposition";
import {CircularProgress, Grid} from "@mui/material";
import StatExposition from "../../components/Exposition/StatExposition";
import ImageListItem from "@mui/material/ImageListItem";


let pages = [
    {
        'name': 'Выставки',
        'link': `/frontend/api/exposition_list?is_archive=${0}`
    },
    {'name': 'Архив', 'link': `/frontend/api/exposition_list?is_archive=${1}`},
    {'name': 'Статистика', 'link': `/frontend/api/exposition_list`},
]

function ExpositionListPage(props) {
    const host = process.env.REACT_APP_HOST_NAME
    const auth = useAuth()
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);
    const [value, setValue] = React.useState(0);

    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
            setData(data);
            setFetchAll(true);
        })
    }, [value])

    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>

            <Header
                auth={auth}
                pages={pages}
                mainLink={`${host}/frontend/main/`}
                activePage={(newValue) => (setValue(newValue))}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                {function () {

                    if (fetchAll) {
                        switch (pages[value]['name']) {
                            case "Выставки":
                                return (
                                    <Box sx={{display:'flex'}}>
                                            <Grid container spacing={2}
                                                  sx={{justifyContent: data.length>2?'space-between':'flex-start'}}>
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
                            case "Архив":
                                return (
                                    data.map((item, index) => (
                                        <ImageListItem key={index}
                                                       sx={{marginTop: '25px'}}>
                                            <CardExposition key={index}
                                                            data={item}/>
                                        </ImageListItem>
                                    ))
                                )
                            case "Статистика":
                                return (
                                    <StatExposition data={data}/>
                                )

                        }
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


            </Container>
        </Box>

    )
}

export default ExpositionListPage