import * as React from 'react';
import Box from '@mui/material/Box';
import Tabs, {tabsClasses} from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';

export default function VerticalTabs(props) {
    const [value, setValue]= React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
        props.setValueVerticalTabs(newValue)
    };

    return (
        <Box
            sx={{
                maxWidth: {xs: 320, sm: 480},
                height: 90,
                bgcolor: 'background.paper',
                display: 'flex',
            }}
        >

            <Tabs
                value={value}
                onChange={handleChange}
                orientation="vertical"
                variant="scrollable"
                scrollButtons
                aria-label="visible arrows tabs example"
                sx={{
                    [`& .${tabsClasses.scrollButtons}`]: {
                        'height': 20,
                    },
                }}>

                {
                    props.data.map((item, index) => (
                        <Tab label={item} value={index}
                             key={index}/>
                    ))
                }

            </Tabs>

        </Box>
    );
}
