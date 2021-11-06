import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { UserService } from 'src/app/services/user.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;
  
  constructor(private formBuilder: FormBuilder, 
    private router: Router, private _snackBar: MatSnackBar,
    private userService: UserService
    ) { }

  ngOnInit() {
    this.registerForm = this.formBuilder.group({
      firstname: ['', Validators.required],
      lastname: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  get data() { return this.registerForm.controls; }

  onSubmit() {    
    if (this.registerForm.invalid) {
      return;
    } else {
      
      this.userService.register(this.registerForm.value);
    }
  }
}