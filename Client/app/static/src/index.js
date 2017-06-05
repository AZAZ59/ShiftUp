/**
 * Created by vlad on 16.11.16.
 */

import React from 'react';
import ReactDOM from 'react-dom';
require('./css/style.css');
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();
import { MuiThemeProvider } from 'material-ui';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme';
/*require('./fonts/glyphicons-halflings-regular.eot');
require('./fonts/glyphicons-halflings-regular.svg');
require('./fonts/glyphicons-halflings-regular.ttf');
require('./fonts/glyphicons-halflings-regular.woff');
require('./fonts/glyphicons-halflings-regular.woff2');*/

// Notice that we've organized all of our routes into a separate file.
import Routers from './router';
class App extends React.Component{
    render(){
        return(
            <MuiThemeProvider>
                <Routers />
            </MuiThemeProvider>
            )
    }
}

// Now we can attach the router to the 'root' element like this:
ReactDOM.render(
    <App/>,
    document.getElementById('root')
);
