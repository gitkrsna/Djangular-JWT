import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StudentRegistrationForm } from './student-registration.component';

describe('StudentRegistrationForm', () => {
  let component: StudentRegistrationForm;
  let fixture: ComponentFixture<StudentRegistrationForm>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StudentRegistrationForm ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StudentRegistrationForm);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
