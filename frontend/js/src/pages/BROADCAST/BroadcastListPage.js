import Box from "@mui/material/Box";
import React, {useEffect} from "react";
import Header from "../../components/Header/Header";
import {Grid} from "@mui/material";
import Container from "@mui/material/Container";
import dataFetch from "../../components/utils/dataFetch"
import ItemBroadcast from "../../components/Broadcast/ItemBroadcast";
import useAuth from "../../components/hooks/useAuth";


let pages = [
    {'name': 'Вебинары', 'link': '/frontend/api/events/'},
]

const host = process.env.REACT_APP_HOST_NAME

function BroadcastListPage() {
    const auth = useAuth()
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);


    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
            setData(data);
        })
    }, [])

    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
            setData(data);
        })
    }, [value])


    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header pages={pages}
                    activePage={(newValue) => (setValue(newValue))}
                    auth={auth}
                    mainLink={`${host}/frontend/main/`}/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>
                <Box>
                    <Grid container spacing={2}
                          sx={{justifyContent: 'space-between'}}>
                        {data.map((item, index) => (
                            item['broadcast_url'] ?
                                <Grid item xs="auto" key={index}>
                                    <ItemBroadcast data={item}/>
                                </Grid> : ''
                        ))}

                    </Grid>
                </Box>

            </Container>
        </Box>

    )
}

export default BroadcastListPage