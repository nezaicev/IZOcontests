import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import Header from "../../components/Header/Header";
import {Grid} from "@mui/material";
import CardEvent from "../../components/Event/CardEvent";
import Container from "@mui/material/Container";
import dataFetch from "../../components/utils/dataFetch"
import useAuth from "../../components/hooks/useAuth";
import ItemBroadcast from "../../components/Broadcast/ItemBroadcast";
import {useNavigate, useLocation, redirect} from "react-router-dom";
import CardContest from "../../components/Contest/CardContest";


let pages = [
    {'name': 'Конкурсы', 'link': '/frontend/api/contests/'},
    {'name': 'Мероприятия', 'link': '/frontend/api/events/'},
    {'name': 'Вебинары', 'link': '/frontend/api/broadcasts/'},
    {'name': 'Выставки', 'link': ''},
    {'name': 'Виртуальный музей', 'link': 'http://shkola-nemenskogo.ru/'}

]

const host = process.env.REACT_APP_HOST_NAME

function MainPage() {
    const navigate = useNavigate()
    const location = useLocation()
    const auth = useAuth()
    const [fetchAll, setFetchAll] = useState(false);
    const [participantEvent, setParticipantEvent] = React.useState([])
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);


    function renderData() {
        switch (pages[value]['name']) {
            case "Мероприятия":
                return (
                     <Box sx={{
                                    display: 'grid',
                                    gridTemplateColumns: `repeat(auto-fill, minmax(320px, 1fr))`,
                                    justifyItems: 'center',
                                    alignItems: 'stretch',
                                    marginBottom: '60px',

                                }}>
                        {data.length>0 ?function () {
                            if (fetchAll || !auth['auth']) {
                                return (
                                    data.map((item, index) => (
                                        <Grid item xs="auto" sx={{margin:'20px'}}
                                              key={index}>
                                            <CardEvent
                                                data={item}
                                                auth={auth}
                                                participantEvent={participantEvent}
                                            />
                                        </Grid>
                                    )))
                            }
                        }():''

                        }
                     </Box>
                )
            case "Конкурсы":
                return (
                     <Box sx={{
                                    display: 'grid',
                                    gridTemplateColumns: `repeat(auto-fill, minmax(320px, 1fr))`,
                                    justifyItems: 'center',
                                    alignItems: 'stretch',
                                    marginBottom: '30px',

                                }}>
                        {function () {
                            if (fetchAll || !auth['auth']) {
                                return (
                                    data.map((item, index) => (
                                        <Grid item xs="auto" sx={{margin:'20px'}}
                                              key={index}>
                                            <CardContest
                                                data={item}
                                                auth={auth}
                                            />
                                        </Grid>
                                    )))
                            }
                        }()

                        }
                     </Box>
                )
            case "Вебинары":
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

                     </Box>
                )
            case "Выставки": {
                return (navigate("/frontend/expositions/"))
            }
            case "Виртуальный музей": {
                document.location.href = 'http://shkola-nemenskogo.ru/'
            }

        }
    }

    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {

            setData(data)

        })



    }, [])


    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {

            setData(data);
        })
    }, [value])


    useEffect(() => {
        if (auth['id']) {
            dataFetch(`${host}/frontend/api/participant_event_list/`, {'participant': auth['id']}, (data) => {
                setParticipantEvent(data.map((item) => (Number(item['event']))))
                setFetchAll(true)

            })
        }
    }, [auth])


    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header pages={pages}
                    activePage={(newValue) => (setValue(newValue))}
                    auth={auth}
                    mainLink={`${host}/frontend/main/`}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>
                <Box sx={{justifyContent: 'center'}}>

                    {renderData()}

                </Box>


            </Container>
        </Box>

    )
}

export default MainPage