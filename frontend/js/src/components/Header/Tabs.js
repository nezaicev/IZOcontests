// import * as React from 'react';
// import PropTypes from 'prop-types';
// import Tabs from '@mui/material/Tabs';
// import Tab from '@mui/material/Tab';
// import Typography from '@mui/material/Typography';
// import Box from '@mui/material/Box';
//
//
//
// function a11yProps(index) {
//   return {
//     id: `simple-tab-${index}`,
//     'aria-controls': `simple-tabpanel-${index}`,
//   };
// }
//
// export default function MainTabs(props) {
//   const [value, setValue] = React.useState(0);
//
//   const handleChange = (event, newValue) => {
//     setValue(newValue);
//   };
//
//   return (
//     <Box sx={{ width: '100%' }}>
//       <Box sx={{  }}>
//         <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
//           {  props.tabs.map((tab, index) =>(
//             <Tab label={tab['name']} {...a11yProps(index)} />
//           ))}
//
//         </Tabs>
//       </Box>
//
//     </Box>
//   );
// }
