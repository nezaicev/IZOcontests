import Box from "@mui/material/Box";
import React from "react";
import Header from "../../components/Header/Header";
import {Grid} from "@mui/material";
import CardEvent from "../../components/Event/CardEvent";
import CardExposition from "../../components/Exposition/CardExposition";
import Container from "@mui/material/Container";


let pages = [
    {'name': 'Мероприятия','link': '#'},
    {'name': 'Конкурсы','link': '#'},
    {'name': 'Выставки','link': '#'}

]


function MainPage() {

    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header pages={pages}/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>
                <Box>
                    <Grid container spacing={2}
                          sx={{justifyContent: 'space-between'}}>
                        <Grid item xs="auto">
                            <CardEvent/>
                        </Grid>
                        <Grid item xs="auto">
                            <CardEvent/>
                        </Grid>
                        <Grid item xs="auto">
                            <CardEvent/>
                        </Grid>
                        <Grid item xs="auto">
                            <CardEvent/>
                        </Grid>
                    </Grid>
                </Box>

                <Box>
                    <Grid container spacing={2}
                          sx={{justifyContent: 'space-between'}}>
                        <Grid item xs="auto">
                            <CardExposition/>
                        </Grid>
                        <Grid item xs="auto">
                            <CardExposition/>
                        </Grid>
                        <Grid item xs="auto">
                            <CardExposition/>
                        </Grid>
                        <Grid item xs="auto">
                            <CardExposition/>
                        </Grid>
                    </Grid>
                </Box>

            </Container>
        </Box>

    )
}

export default MainPage