import Box from "@mui/material/Box";
import { CircularProgress, Paper, Typography} from "@mui/material";
import LocationOnIcon from '@mui/icons-material/LocationOn';
import React, {useEffect, useState} from "react";
import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import {optionsSRLWrapper} from "../../components/styled";
import ImageListItem from "@mui/material/ImageListItem";
import Card from "@mui/material/Card";
import {host} from "../../components/utils/consts";
import {useParams} from "react-router-dom";
import dataFetch from "../../components/utils/dataFetch";




function Exposition(props) {
    const [fetchAll, setFetchAll] = useState(false);
    const [value, setValue] = React.useState(0);
    const [data, setData] = React.useState({})
    let {id} = useParams()

    useEffect(() => {
        dataFetch(`${host}/frontend/api/exposition/${id}/`, null, (data) => {
            setData(data);
            setFetchAll(true)
        })
    }, [])


    return (
        <Box>
            {fetchAll ? <Box>
                <Box sx={{
                    justifyContent: 'center',
                    display: 'flex',
                    marginTop: '15px',
                    marginBottom: '15px'
                }}>
                    <Typography variant="h5">
                        {data.title}
                    </Typography>
                </Box>
                <Box sx={{marginTop: '15px', marginBottom: '5px'}}>


                    <Box sx={{
                        display: 'flex'
                    }}>
                        <LocationOnIcon
                            sx={{color: 'rgb(128,110,110)'}}/>
                        <Typography sx={{fontSize: [10, 12, 14]}} variant="overline" display="block"
                                    gutterBottom>
                            {data.address}
                        </Typography>
                    </Box>


                </Box>

                <Paper

                    dangerouslySetInnerHTML={{__html: data.content}}
                    scroll={'body'}
                    sx={{
                        boxShadow: 0,
                        maxHeight: 600,
                        overflow: 'auto',
                        padding: ['5px', '15px'],
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

                                {fetchAll ? data.images.map((item, index) => (

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
                                                    alt={item.label ? item.label : data.title}
                                                    loading="lazy"
                                                />
                                            </a>
                                        </Card>
                                    </ImageListItem>)) : null}
                            </Box>
                        </SRLWrapper>
                    </SimpleReactLightbox>


                </Box>

            </Box> : <Box sx={{
                justifyContent: 'center',
                height: '600',
                display: 'flex',
                marginTop: ' 20px'
            }}>
                <CircularProgress sx={{
                    color: '#d26666'
                }}/>
            </Box>
            }

        </Box>

    )
}


export {Exposition}

