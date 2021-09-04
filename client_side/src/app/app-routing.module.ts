import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NavBarComponent } from './layouts/nav-bar/nav-bar.component';
import { SignupLoginComponent } from './signup-login/signup-login.component';
import { AuthguardService as AuthGuard } from './services/gaurds/authguard.service';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { HomepageComponent } from './homepage/homepage.component';
import { LoginGaurdService as LoginGuard } from './services/gaurds/login-gaurd.service';
import { StudentComponent } from './student/student.component';
const routes: Routes = [
  { path: '', component: HomepageComponent },
  { path: 'home', component: NavBarComponent, canActivate: [AuthGuard] },
  { path: 'students', component: StudentComponent, canActivate: [AuthGuard] },
  { path: 'login', component: SignupLoginComponent, canActivate: [LoginGuard] },

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
