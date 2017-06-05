/**
 * Created by vlad on 21.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';


class GetMembersRelations extends React.Component{
    method_name = 'Collector.Groups.get_members_relations';
    default_state = {group_id: ''};

    constructor(props) {
        super(props);
        this.state = this.default_state;
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({group_id: event.target.value});
    }


    handleSubmit(event) {
        if(this.state.group_id.length == 0){
            alert('Error!')
        }
        else {
            send_task(this.method_name, {
                'group_id': this.state.group_id
            });
        }
        this.setState(this.default_state);
        event.preventDefault();
    }

    render(){
        return(
            <div class = 'content'>
                <div className="page-header">
                    <h1>Сбор пар подписчиков</h1>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup
                        controlId="formBasicText"
                    >
                        <ControlLabel>Введите ссылку на сообщество:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.group_id}
                            placeholder="coffman"
                            onChange={this.handleChange}
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

export default GetMembersRelations

