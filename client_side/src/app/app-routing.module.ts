import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NavBarComponent } from './layouts/nav-bar/nav-bar.component';
import { SignupLoginComponent } from './signup-login/signup-login.component';
import { AuthguardService as AuthGuard } from './services/gaurds/authguard.service';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { FeesComponent } from './fees/fees.component';
import { LoginGaurdService as LoginGuard } from './services/gaurds/login-gaurd.service';
import { StudentComponent } from './student/student.component';
import { CreateStudentRegistration } from './student-registration/student-registration.component';
import { AppComponent } from './app.component';
import { BlogPostComponent } from './blog-post/blog-post.component';

const routes: Routes = [
  //{ path: '', component: AppComponent, canActivate: [AuthGuard] },
  //{ path: '', component: NavBarComponent, canActivate: [AuthGuard] },
  { path: 'students', component: StudentComponent, canActivate: [AuthGuard] },
  { path: 'fees', component: FeesComponent, canActivate: [AuthGuard] },
  { path: 'login', component: SignupLoginComponent, canActivate: [LoginGuard] },
  { path: 'student-registration', component: CreateStudentRegistration, canActivate: [AuthGuard]},
  { path: 'blog', component: BlogPostComponent, canActivate: [AuthGuard]},

  // { path: 'second-component', component: SecondComponent },
  // { path: '',   redirectTo: '/first-component', pathMatch: 'full' }, // redirect to `first-component`
  { path: '**', component: PagenotfoundComponent, canActivate: [AuthGuard] }, // Wildcard route for a 404 page
];

@NgModule({
  imports: [RouterModule.forRoot(routes),
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
