/**
 * Created by vlad on 21.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';


class GetUsersPosts extends React.Component{
    method_name = 'Collector.Groups.get_groups_posts';
    default_state = {user_ids: '', count: '', all: true};

    constructor(props) {
        super(props);
        this.state = this.default_state;
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleCountChange = this.handleCountChange.bind(this);
    }

    handleChange(event) {
        this.setState({user_ids: event.target.value});
    }

    handleCountChange(event) {
        if(event.target.value.length > 0){
            this.setState({all: !this.state.all});
        }
        this.setState({count: event.target.value});
    }


    handleSubmit(event) {
        var user_ids = this.state.user_ids.split(',');
        if(this.state.user_ids.length == 0){
            alert('Error!')
        }
        else {
            if(this.state.all){
                send_task(this.method_name, {
                    'user_ids': user_ids
                });
            }
            else {
                send_task(this.method_name, {
                    'user_ids': user_ids,
                    'count': this.state.count
                });
            }
        }
        this.setState(this.default_state);
        event.preventDefault();
    }

    render(){
        return(
            <div class = 'content'>
                <div className="page-header">
                    <h1>Сбор постов пользователей</h1>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup
                        controlId="formBasicText"
                    >
                        <ControlLabel>Введите список людей через запятую:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.user_ids}
                            placeholder="durov, id1"
                            onChange={this.handleChange}
                        />
                        <ControlLabel>Какое кол-во постов выгрузить:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.count}
                            placeholder="По-умолчанию все посты"
                            onChange={this.handleCountChange}
                        />
                    </FormGroup>
                    <Button type="submit">
                        Отправить
                    </Button>
                </form>
            </div>
        );
    }
};

export default GetUsersPosts
