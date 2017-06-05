/**
 * Created by vlad on 16.11.16.
 */

var React = require('react');
var Link = require('react-router').Link;
import Menu from './menu'
import Header from './header'
import { Paper } from 'material-ui';
import store from '../store'

class MainLayout extends React.Component{
    constructor(...args) {
        super(...args);

    }
    render(){
        return (
            <div>
                <Header/>
                <Paper>
                    {this.props.children}
                </Paper>
            </div>
        );
    }
};

export default MainLayout;
