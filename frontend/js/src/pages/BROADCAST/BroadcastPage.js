import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import dataFetch from "../../components/utils/dataFetch"
import {useParams} from "react-router-dom";
import ReactPlayer from "react-player/youtube";
import Typography from "@mui/material/Typography";
import {getFormattedDate} from "../../components/utils/utils";
import {CircularProgress, Paper} from "@mui/material";
import Divider from "@mui/material/Divider";


let pages = [
    {'name': 'Трансляции', 'link': '/frontend/api/broadcast/'},
]

const host = process.env.REACT_APP_HOST_NAME

function BroadcastPage() {

    let {id} = useParams();
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);
    const [isFetching, setIsFetching] = useState(true);


    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}${id}/`, null, (data) => {
            setData(data);
        }, (value)=>(setIsFetching(value)))
        console.log(isFetching)
    }, [])

    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header pages={pages}
                    activePage={(newValue) => (setValue(newValue))}/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>
                {isFetching ?  <Box sx={{
                                    justifyContent: 'center',
                                    height:'600',
                                    display: 'flex',
                                    marginTop: ' 20px'
                                }}>
                                    <CircularProgress sx={{
                                        color: '#d26666'
                                    }}/>
                                </Box> :  <Box>
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
                </Box>}

            </Container>
        </Box>

    )
}

export default BroadcastPage