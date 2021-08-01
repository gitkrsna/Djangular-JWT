import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BlogPostService } from '../services/blog_post.service';
import { UserService } from '../services/user.service';
import { throwError } from 'rxjs'; // Angular 6/RxJS 6

@Component({
  selector: 'app-signup-login',
  templateUrl: './signup-login.component.html',
  styleUrls: ['./signup-login.component.scss'],
})
export class SignupLoginComponent implements OnInit {
  /**
   * An object representing the user for the login form
   */
  public user: any;

  /**
   * An array of all the BlogPost objects from the API
   */
  public posts;

  /**
   * An object representing the data in the "add" form
   */
  public new_post: any;

  constructor(
    private blogPostService: BlogPostService,
    private router: Router,
    private userService: UserService
  ) {}

  usertoken: any;
  ngOnInit() {
    this.getPosts();
    this.new_post = {
      body: '',
    };
    this.user = {
      username: '',
      password: '',
    };
  }

  login() {
    this.userService.login({
      username: this.user.username,
      password: this.user.password,
    });
  }

  refreshToken() {
    this.userService.refreshToken();
  }

  logout() {
    this.userService.logout();
  }

  getPosts() {
    this.blogPostService.list().subscribe(
      // the first argument is a function which runs on success
      (data) => {
        this.posts = data;
        // convert the dates to a nice format
        for (let post of this.posts.results) {
          post.date = new Date(post.date);
        }
      },
      // the second argument is a function which runs on error
      (err) => console.error(err),
      // the third argument is a function which runs on completion
      () => console.log('done loading posts')
    );
  }

  createPost() {
    this.blogPostService.create(this.new_post, this.user.token).subscribe(
      (data) => {
        // refresh the list
        this.getPosts();
        return true;
      },
      (error) => {
        console.error('Error saving!');
        return throwError(error);
      }
    );
  }
}
