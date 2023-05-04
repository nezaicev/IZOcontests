import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import Header from "../../components/Header/Header";
import {CircularProgress, Grid, Paper, Typography} from "@mui/material";
import Container from "@mui/material/Container";
import dataFetch from "../../components/utils/dataFetch"
import useAuth from "../../components/hooks/useAuth";
import {useNavigate, useLocation, Route, Routes, useParams} from "react-router-dom";
import GalleryMyMoskvichi from "../../components/Gallary/MyMoskvichi/GalleryMyMoskvichi";
import Doctor from "../../components/CustomIcons/Doctor";
import Button from "@mui/material/Button";
import Map from "../../components/CustomIcons/Map";
import Museum from "../../components/CustomIcons/Museum";
import {BaseInfo} from "./BaseInfo";


let pages = [
    {'name': 'Мы Москвичи', 'link': '/frontend/api/page/mymoskvichi_base_info/'},
    {'name': 'Положение', 'link': '/frontend/api/page/mymoskvichi_pologenie_2023/'},
    {'name': 'Галерея', 'link': ''},
    {'name': 'Жюри конкурса', 'link': '/frontend/api/page/mymoskvichi_gury/'},
]






const host = process.env.REACT_APP_HOST_NAME

function MainPage() {

    const navigate = useNavigate()
    const location = useLocation()
    const auth = useAuth()
    const [fetchAll, setFetchAll] = useState(false);
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(useParams()?Number(useParams()['slug']):0);


    function renderData() {
        switch (pages[value]['name']) {
            case "Мы Москвичи":
                return (<Box>
                        <Box>
                            <BaseInfo/>
                        </Box>
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
                    </Box>

                )
            case "Положение":
            case "Жюри конкурса": {

                return (<Box>{
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
                                // maxHeight: 600,
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
                }</Box>)
            }
            case "Галерея": {
                return (<GalleryMyMoskvichi
                    contestName={process.env.REACT_APP_MYMOSKVICHI}
                    urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                    urlHorizontalTabs={`${host}/frontend/api/archive/contest/nominations/`}
                    // urlCreativeTack={`${host}/frontend/api/contest/creative_tack/`}
                    urlContent={`${host}/frontend/api/archive/`}
                />)
            }

            case "Проект «Мой любимый край»":
            case "СПАСИБО ВРАЧАМ!":
            case "АРТ-КВЕСТЫ «Путешествие по виртуальным музеям»": {
                return (function () {
                    window.location.href = pages[value]['link']
                }())

            }

        }
    }


    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
                setData(data);
                setFetchAll(true)
            })
    }, [])


    useEffect(() => {
        if (pages[value]['link'] !== '') {
            dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
                setData(data);
                setFetchAll(true)
            })
        }

    }, [value])


    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header pages={pages}
                    activePage={(newValue) => (setValue(newValue))}
                    startPage={value}
                    auth={auth}
                    mainLink={`${host}/frontend/main/`}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>


                {renderData()}


            </Container>
        </Box>

    )
}

export default MainPage