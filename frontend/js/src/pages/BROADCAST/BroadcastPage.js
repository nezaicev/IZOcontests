import Box from "@mui/material/Box";
import React, {useEffect} from "react";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import dataFetch from "../../components/utils/dataFetch"
import {useParams} from "react-router-dom";
import ReactPlayer from "react-player/youtube";
import Typography from "@mui/material/Typography";
import {getFormattedDate} from "../../components/utils/utils";
import {Paper} from "@mui/material";
import Divider from "@mui/material/Divider";
import {DividerStyled} from "../../components/styled";


let pages = [
    {'name': 'Трансляции', 'link': '/frontend/api/broadcast/'},
]

const host = process.env.REACT_APP_HOST_NAME

function BroadcastListPage() {
    let {id} = useParams();
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);


    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}${id}/`, null, (data) => {
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
                    activePage={(newValue) => (setValue(newValue))}/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>
                <Box>
                    <Box sx={{}}>
                        <Typography variant="button" display="block"
                                    gutterBottom>
                            {data['name']}
                        </Typography>
                        <Typography variant="subtitle2" gutterBottom>
                         Начало: {getFormattedDate(data['start_date'])}
                        </Typography>
                    </Box>
                    <Divider sx={{marginTop:'10px', marginBottom:'10px'}}/>

                    <div className="player-wrapper">
                        <ReactPlayer
                            className='react-player'
                            controls={true}
                            url={data['broadcast_url']}
                            width='100%'
                            height='100%'
                        />
                    </div>
                </Box>

            </Container>
        </Box>

    )
}

export default BroadcastListPage