import React, {useEffect, useState} from "react";
import {Grid} from "@mui/material";
import CardEvent from "../../components/Event/CardEvent";
import Box from "@mui/material/Box";
import {useOutletContext} from "react-router-dom";
import dataFetch from "../../components/utils/dataFetch";


const Events = () => {
    const apiLink = '/frontend/api/events/'

    const [fetchAll, setFetchAll] = useState(false);
    const [data, setData] = React.useState([])
    const [participantEvent, setParticipantEvent] = React.useState([])
    const auth = useOutletContext()

    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {order:'start_date'}, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [])

    useEffect(() => {
        if (auth['id']) {
            dataFetch(`${process.env.REACT_APP_HOST_NAME}/frontend/api/participant_event_list/`, {'participant': auth['id']}, (data) => {
                setParticipantEvent(data.map((item) => (Number(item['event']))))
                setFetchAll(true)

            })
        }
    }, [auth])


    return (

        <>
            {data.length > 0 ? function () {
                if (fetchAll) {
                    return (<Box sx={{
                            display: 'grid',
                            gridTemplateColumns: `repeat(auto-fill, minmax(320px, 1fr))`,
                            justifyItems: 'center',
                            alignItems: 'stretch',
                            marginBottom: '60px',

                        }}>
                            {data.map((item, index) => (
                            <Grid item xs="auto" sx={{margin: '20px'}}
                                  key={index}>
                                <CardEvent
                                    data={item}
                                    auth={auth}
                                    participantEvent={participantEvent}
                                />
                            </Grid>
                            ))}
                        </Box>
                    )

                }
            }() : ''

            }


        </>


    )
}

export {Events}