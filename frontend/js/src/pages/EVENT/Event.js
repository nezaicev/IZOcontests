import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import React, {useEffect, useState} from "react";
import Typography from "@mui/material/Typography";
import {useOutletContext, useParams} from "react-router-dom";
import useAuth from "../../components/hooks/useAuth";
import dataFetch from "../../components/utils/dataFetch";
import {host} from "../../components/utils/consts";
import CardEvent from "../../components/Event/CardEvent";
import {Grid} from "@mui/material";



function Event(props) {

    const auth = useOutletContext()
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


    )
}

export default Event