import { ChangeDetectorRef, Component, Inject, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { StudentService } from '../services/student.service';
import { DialogData } from '../student-registration/student-registration.component';
import {FormControl} from '@angular/forms';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';
@Component({
  selector: 'app-fees',
  templateUrl: './fees.component.html',
  styleUrls: ['./fees.component.scss']
})
export class FeesComponent implements OnInit {
  feesList : any = [];
  displayedColumns = [];
  studentList: any;
  constructor(public dialog: MatDialog,
    private studentService: StudentService,
    private changeDetectorRef: ChangeDetectorRef) {}
  ngOnInit(): void {
    this.studentService.listFees().subscribe(response => {
      this.displayedColumns = ['First Name', 'Last Name', 'Father\'s Name', 
      'Mother\'s Name', 'Course', 'Enrollment Date',
      'Fees Month', 'Amount'];
       this.feesList = response;
       console.log(response);
     })
    }
  openDialog(): void {
    this.studentService.list().subscribe(response => {
      this.studentList = response;
    })

    const dialogRef = this.dialog.open(SubmitFeesForm, {
      width: '18rem',
      height: '60%',
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
}


@Component({
  selector: 'app-submit-fees',
  templateUrl: './submit-fees.component.html',
  styleUrls: ['./fees.component.scss']
})
export class SubmitFeesForm implements OnInit {

  myControl = new FormControl();
  options: any;
  Months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',  
    'May', 
    'Jun', 
    'Jul', 
    'Aug', 
    'Sep', 
    'Oct', 
    'Nov', 
    'Dec',
];
Amounts = [100, 150, 200, 250, 300, 350, 400, 450, 500];
  ngOnInit() {

    this.studentService.list().subscribe(x  => {
     this.options = x;
    })
    
  }

  fees = {
    student: '',
    fees_month: '',
    amount: ''
  }
  feesList : any = [];
  constructor(
    public dialogRef: MatDialogRef<SubmitFeesForm>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,
    private studentService: StudentService,
    private changeDetectorRef: ChangeDetectorRef,
    private router: Router) {}

  onCancelClick(): void {
    this.dialogRef.close();
  }

  saveFeesDetails(){
    this.studentService.submitFees(this.fees).subscribe(response => {
      this.feesList = response;
      this.dialogRef.close();
      this.router.navigate(['/fees']);
    })
   }
}
