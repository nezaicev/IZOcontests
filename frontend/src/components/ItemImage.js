import * as React from "react";
import Box from "@mui/material/Box";

import {

    ImageButton,

} from "../styled";


export function ItemImage(props) {

    const image = props.image

    return (<React.Fragment>


            <ImageButton sx={{
                p: '10px',
                margin: '10px',
                backgroundColor: '#ffffff'
            }}
                         key={props.index}
                         ref={(props.lastElementRef) ? props.lastElementRef : undefined}
            >

                <Box component='div' key={props.index}>
                    <a href={image['md_thumb']}>
                        <img
                            src={image['thumb']}
                            alt={props.label}
                            loading="lazy"

                        />

                    </a>
                </Box>


            </ImageButton>


        </React.Fragment>
    )


}