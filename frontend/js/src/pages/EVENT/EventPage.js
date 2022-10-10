import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import React, {useEffect, useState} from "react";
import Typography from "@mui/material/Typography";
import {useParams} from "react-router-dom";
import useAuth from "../../components/hooks/useAuth";
import dataFetch from "../../components/utils/dataFetch";
import {host} from "../../components/utils/consts";
import CardEvent from "../../components/Event/CardEvent";
import {Grid} from "@mui/material";

let pages = [
    {'name': 'Мероприятия', 'link': '/frontend/api/events/'},


]


function EventPage(props) {

    const auth = useAuth()
    let {id} = useParams();
    const [fetchAll, setFetchAll] = useState(false);
    const [participantEvent, setParticipantEvent] = React.useState([])
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);


    useEffect(() => {
        dataFetch(`${host}/frontend/api/event/${id}/`, null, (data) => {
            setData([data]);
        })
    }, [])
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
                justifyContent: 'center'
            }}>
                <Box sx={{display: 'flex'}}>
                    {function () {
                        if (fetchAll || !auth['auth']) {
                            return (
                                data.map((item, index) => (

                                            <CardEvent data={item}
                                                       auth={auth}
                                                       participantEvent={participantEvent}/>

                                    ))

                            )
                        }
                    }()

                    }
                </Box>

            </Container>
        </Box>

    )
}

export default EventPage