import Box from "@mui/material/Box";
import {Chip, CircularProgress, Paper, Typography} from "@mui/material";
import LocationOnIcon from '@mui/icons-material/LocationOn';
import React, {useEffect, useState} from "react";
import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import {optionsSRLWrapper} from "../../components/styled";
import ImageListItem from "@mui/material/ImageListItem";
import Card from "@mui/material/Card";
import {createLabel} from "../../components/utils/utils";
import Header from "../../components/Header/Header";
import {host} from "../../components/utils/consts";
import Container from "@mui/material/Container";
import {useParams} from "react-router-dom";
import useAuth from "../../components/hooks/useAuth";
import dataFetch from "../../components/utils/dataFetch";

let pages = [
    {'name': 'Выставки', 'link': '/frontend/api/events/'},
    // {'name': 'Архив', 'link': '/frontend/api/events/'},
    // {'name': 'Статистика', 'link': '/frontend/api/events/'}

]

function ExpositionPage(props) {
    const auth = useAuth()
     const [fetchAll, setFetchAll] = useState(false);
     const [value, setValue] = React.useState(0);
    const [data, setData]=React.useState({})
    let {id}=useParams()

     useEffect(() => {
        dataFetch(`${host}/frontend/api/exposition/${id}/`, null, (data) => {
            setData(data);
            setFetchAll(true)
        })
    }, [])



    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header pages={pages}
                    activePage={(newValue) => (setValue(newValue))}
                    auth={auth}
                    mainLink={`${host}/frontend/expositions/`}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                {fetchAll ?  <Box>
                    <Box sx={{justifyContent:'center', display:'flex', marginTop:'15px', marginBottom:'15px'}}>
                        <Typography variant="h5">
                            {data.title}
                        </Typography>
                    </Box>
                    <Box sx={{marginTop:'15px', marginBottom:'5px'}}>
                    <Chip icon={<LocationOnIcon sx={{color: 'rgb(128,110,110)'}}/>}
                          label={data.address}/>
                    </Box>

                     <Paper

                     dangerouslySetInnerHTML={{__html: data.content}}
                     scroll={'body'}
                     sx={{
                         boxShadow: 0,
                         maxHeight:600,
                         overflow:'auto',
                         padding:['5px','15px'],
                     }}

                />
                    <Box>

                        <SimpleReactLightbox>
                            <SRLWrapper options={optionsSRLWrapper}>
                                <Box sx={{
                                    display: 'grid',
                                    gridTemplateColumns: `repeat(auto-fill, minmax(320px, 1fr))`,
                                    justifyItems: 'center',
                                    alignItems: 'center',
                                    marginBottom: '30px',

                                }}>

                                    { fetchAll ? data.images.map((item, index) => (

                                        <ImageListItem key={index}
                                                       sx={{marginTop: '25px'}}>
                                            <Card sx={{
                                                border: 7,
                                                borderColor: '#fff',
                                                boxShadow: 0
                                            }}
                                                  key={index}
                                            >
                                                <a href={item['md_thumb']}>
                                                    <img
                                                        src={item['thumb']}
                                                        alt={data.title}
                                                        loading="lazy"
                                                    />
                                                </a>
                                            </Card>
                                        </ImageListItem>)):null}
                                </Box>
                            </SRLWrapper>
                        </SimpleReactLightbox>


                    </Box>

                </Box>: <Box sx={{
                                    justifyContent: 'center',
                                    height:'600',
                                    display: 'flex',
                                    marginTop: ' 20px'
                                }}>
                                    <CircularProgress sx={{
                                        color: '#d26666'
                                    }}/>
                                </Box>
                               }



            </Container>
        </Box>


    )
}


export default ExpositionPage

