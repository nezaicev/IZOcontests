import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import ImageListItem from "@mui/material/ImageListItem";
import React from "react";
import {ImageListStyled, optionsSRLWrapper} from "../styled";

import Box from "@mui/material/Box";
import ImageList from "@mui/material/ImageList";


export default function ImageGallery(props) {
    const images = props.images
    const title = props.titleImg

    return (
        <SimpleReactLightbox>
            <SRLWrapper options={optionsSRLWrapper}>
                <Box sx={{
                    display: 'grid',
                    gridTemplateColumns: `repeat(auto-fill, minmax(300px, 1fr))`,
                    justifyItems: 'center',
                    alignItems: 'center',
                    marginBottom: '30px',

                }}>

                    {images.map((item, index) => (

                        <ImageListItem key={index} sx={{marginTop: '25px'}}
                        >

                            <a href={item['md_thumb']}>
                                <img
                                    src={item['thumb']}
                                    alt={title}
                                    loading="lazy"
                                />

                            </a>
                        </ImageListItem>


                    ))}

                </Box>


            </SRLWrapper>
        </SimpleReactLightbox>)
}