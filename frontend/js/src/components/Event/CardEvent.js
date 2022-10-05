import Card from "@mui/material/Card";

import {CardMedia, Chip, Paper} from "@mui/material";
import Box from "@mui/material/Box";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import FieldTitle from "../Gallary/FieldTitle";
import React, {useEffect} from "react";
import EventNoteIcon from '@mui/icons-material/EventNote';
import Button from "@mui/material/Button";
import {brown} from '@mui/material/colors';
import {ButtonDefault, DividerStyled} from "../styled";
import {getFormattedDate} from "../utils/utils";
import {host} from "../utils/consts";
import dataFetch from "../utils/dataFetch";
import dataDelete from "../utils/dataDelete";
import dataPut from "../utils/dataPut";

const buttonColor = brown.A400


// function getButtonCardEvent(userId, eventId, auth, participantEvent, setParticipantEventList) {
//
//
//     if (auth) {
//         // setParticipantEventList()
//         if (participantEvent.includes(eventId)) {
//
//             return <Box>
//                 Заявка на участие принята
//                 <ButtonDefault onClick={() => {
//                     dataDelete(`${host}/frontend/api/participant_event/`, {
//                         'participant': userId,
//                         'event': eventId
//                     });
//
//
//                 }} variant="outlined" size='small'>
//                     Отменить
//                 </ButtonDefault>
//             </Box>
//         } else {
//             return <ButtonDefault onClick={() => {
//                 dataPut(`${host}/frontend/api/participant_event/`,
//                     {'participant': userId},
//                     {'participant': userId, 'event': eventId})
//
//             }} variant="outlined" size='small'>
//                 Принять участие
//             </ButtonDefault>
//         }
//
//     } else {
//         return <ButtonDefault onClick={() => {
//             window.location.replace(`${host}/users/login/`)
//         }} variant="outlined" size='small'>
//             Необходима авторизация
//         </ButtonDefault>
//     }
//
// }

// function ButtonCardEvent(){
//     const [status, setStatus]=React.useState(
//         <ButtonDefault onClick={() => {
//             window.location.replace(`${host}/users/login/`)
//         }} variant="outlined" size='small'>
//             Необходима авторизация
//         </ButtonDefault>
//     )
// return(
//
// )
//
// }


function CardEvent(props) {

    const statuses = [
            {'auth': false, 'participation': ''},
            {'auth': true, 'participation': true},
            {'auth': true, 'participation': false}
        ]
    const [statusButton, setStatusButton] = React.useState(() => {

        if (props.auth['id']) {
            if (props.participantEvent.includes(props.data['id'])) {
                return statuses[1]
            } else {
                return statuses[2]
            }
        } else {
            return statuses[0]
        }
    })

    return (

        <Card
            sx={{
                display: 'flex',
                flexWrap: 'wrap',
                marginTop: '20px',
                width: 350
            }}>
            <CardMedia
                component="img"
                sx={{
                    width: 350,
                    display: 'block',
                }}
                image={props.data['logo']}
                alt=''
            />

            <Box sx={{
                flexWrap: "wrap",
                flexGrow: 1,
                width: 200,
                display: 'flex',
                justifyContent: 'center',
            }}>

                <CardContent>
                    <Typography variant="body1" display="block" gutterBottom>
                        {props.data['name']}
                    </Typography>
                    <Box component={'div'} sx={{marginTop: '15px'}}>
                        <Chip icon={<EventNoteIcon
                            sx={{color: 'rgb(128,110,110)'}}/>}
                              label={getFormattedDate(props.data['start_date'])}
                              variant="outlined"/>
                    </Box>

                    <Box component={'div'} sx={{margin: '5px'}}>
                        <Typography variant="subtitle1" color="text.secondary"
                                    component="div"
                                    sx={{
                                        alignContent: 'center',
                                        display: 'block',
                                        marginTop: '15px'
                                    }}

                        >
                            {props.data['message']}

                        </Typography>
                    </Box>
                    <DividerStyled/>
                    <Box componetn={'div'} sx={{
                        justifyContent: 'right',
                        display: 'flex',
                        margin: '5px'
                    }}>

                        {
                           function ()  {
                                console.log(statusButton)
                                switch (statusButton) {
                                    case statuses[0]:
                                        return (
                                            <ButtonDefault onClick={() => {
                                                window.location.replace(`${host}/users/login/`)
                                            }} variant="outlined" size='small'>
                                                Необходима авторизация
                                            </ButtonDefault>
                                        )

                                    case statuses[1]:
                                        return (
                                            <Box>
                                                Заявка на участие принята
                                                <ButtonDefault onClick={() => {
                                                    dataDelete(`${host}/frontend/api/participant_event/`, {
                                                        'participant': props.auth['id'],
                                                        'event': props.data['id']
                                                    });
                                                    setStatusButton(statuses[2])
                                                }} variant="outlined"
                                                               size='small'>
                                                    Отменить
                                                </ButtonDefault>
                                            </Box>
                                        )

                                    case statuses[2]:
                                        console.log('test')
                                        return (
                                            <ButtonDefault onClick={() => {
                                                dataPut(`${host}/frontend/api/participant_event/`,
                                                    {'participant': props.auth['id']},
                                                    {
                                                        'participant': props.auth['id'],
                                                        'event': props.data['id']
                                                    })
                                                setStatusButton(statuses[1])
                                            }} variant="outlined" size='small'>
                                                Принять участие
                                            </ButtonDefault>
                                        )

                                }
                            }()
                        }

                        {/*{getButtonCardEvent(props.auth['id'], props.data['id'], props.auth['auth'], props.participantEvent, props.setParticipantEventList)}*/}

                    </Box>


                </CardContent>
            </Box>


        </Card>
    )
}


export default CardEvent