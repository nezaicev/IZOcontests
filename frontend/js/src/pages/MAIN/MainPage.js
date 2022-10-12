import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import Header from "../../components/Header/Header";
import {Grid} from "@mui/material";
import CardEvent from "../../components/Event/CardEvent";
import Container from "@mui/material/Container";
import dataFetch from "../../components/utils/dataFetch"
import useAuth from "../../components/hooks/useAuth";


let pages = [
    {'name': 'Мероприятия', 'link': '/frontend/api/events/'},
    // {'name': 'Виртуальный музей', 'link': '/exposition'}

]

const host = process.env.REACT_APP_HOST_NAME

function MainPage() {


    const auth = useAuth()
    const [fetchAll, setFetchAll] = useState(false);
    const [participantEvent, setParticipantEvent] = React.useState([])
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);

    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
            setData(data);
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
                justifyContent: 'center',
            }}>
                <Box>
                    <Grid container spacing={2}
                          sx={{display:'grid',gridTemplateColumns: 'repeat(3, 1fr)'}}>
                        {function () {
                            if (fetchAll || !auth['auth']) {
                                return (
                                    data.map((item, index) => (
                                        <Grid item xs="auto"  key={index}>
                                            <CardEvent data={item}
                                                       auth={auth}
                                                       participantEvent={participantEvent}
                                            />
                                        </Grid>
                                    )))
                            }
                        }()

                        }


                    </Grid>
                </Box>

                {/*<Box>*/}
                {/*    <Grid container spacing={2}*/}
                {/*          sx={{justifyContent: 'space-between'}}>*/}
                {/*        <Grid item xs="auto">*/}
                {/*            <CardExposition/>*/}
                {/*        </Grid>*/}
                {/*        <Grid item xs="auto">*/}
                {/*            <CardExposition/>*/}
                {/*        </Grid>*/}
                {/*        <Grid item xs="auto">*/}
                {/*            <CardExposition/>*/}
                {/*        </Grid>*/}
                {/*        <Grid item xs="auto">*/}
                {/*            <CardExposition/>*/}
                {/*        </Grid>*/}
                {/*    </Grid>*/}
                {/*</Box>*/}

            </Container>
        </Box>

    )
}

export default MainPage