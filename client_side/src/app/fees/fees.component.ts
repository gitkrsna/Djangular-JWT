import { ChangeDetectorRef, Component, Inject, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { StudentService } from '../services/student.service';
import { DialogData } from '../student-registration/student-registration.component';

@Component({
  selector: 'app-fees',
  templateUrl: './fees.component.html',
  styleUrls: ['./fees.component.scss']
})
export class FeesComponent implements OnInit {
  ngOnInit(): void {
  }

  constructor(public dialog: MatDialog) {}

  openDialog(): void {
    const dialogRef = this.dialog.open(SubmitFeesForm, {
      width: '25rem',
      height: '80%',
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
export class SubmitFeesForm {

  fees = {
    student: 0,
    fees_month: '',
    amount: 0
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
