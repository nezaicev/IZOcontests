import * as React from 'react';
import SvgIcon from '@mui/material/SvgIcon';
import {Button} from "@mui/material";

function HomeIcon(props) {
    return (
        <Button sx={{color:'#fff'}}>
            <SvgIcon {...props}>
                <svg version="1.1" id="Слой_1" x="0px" y="0px"
                     viewBox="0 0 105.9 104.6">
                    <rect x="3.2" y="3.5" fill="#D36666" stroke="#4A4748"
                          width="98.7" height="98.7"/>
                    <line fill="none" stroke="#343333"  x1="30.2"
                          y1="3.5" x2="30.2" y2="79.9"/>
                    <line fill="none" stroke="#343333" x1="76.2"
                          y1="3.5" x2="76.2" y2="79.9"/>*/
                    <line fill="#D36666" stroke="#4A4748"  x1="30.2"
                          y1="41.7" x2="76.2" y2="41.7"/>

                </svg>
            </SvgIcon>
        </Button>

    );
}

export default HomeIcon
