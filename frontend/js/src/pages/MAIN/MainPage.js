import Box from "@mui/material/Box";
import React, {useEffect} from "react";
import Header from "../../components/Header/Header";
import {Grid} from "@mui/material";
import CardEvent from "../../components/Event/CardEvent";
import CardExposition from "../../components/Exposition/CardExposition";
import Container from "@mui/material/Container";
import dataFetch from  "../../components/utils/dataFetch"


let pages = [
    {'name': 'Мероприятия','link': '/frontend/api/events/'},
    {'name': 'Конкурсы','link': '/test'},
    {'name': 'Выставки','link': '/exposition'},
    {'name': 'Виртуальный музей','link': '/exposition'}

]

const host=process.env.REACT_APP_HOST_NAME

function MainPage() {
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);


    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`,null, (data) => {
            setData(data);
        })
    }, [])



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
                        {data.map((item, index)=>(
                            <Grid item xs="auto" key={index}>
                            <CardEvent data={item}/>
                        </Grid>
                        ))}


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